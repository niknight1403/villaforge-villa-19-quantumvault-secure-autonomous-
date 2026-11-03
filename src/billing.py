from fastapi import FastAPI, Request, HTTPException, Depends
import stripe
import os

# Configuration
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

app = FastAPI()

# Tiers mapping
TIER_MAP = {
    "price_standard_id": "STANDARD",
    "price_advanced_id": "ADVANCED",
    "price_quantum_id": "QUANTUM"
}

@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "customer.subscription.updated":
        subscription = event["data"]["object"]
        price_id = subscription["items"]["data"][0]["price"]["id"]
        user_id = subscription["metadata"].get("user_id")
        
        tier = TIER_MAP.get(price_id, "STANDARD")
        # Logic to update user tier in database goes here
        print(f"Updating user {user_id} to tier {tier}")

    return {"status": "success"}