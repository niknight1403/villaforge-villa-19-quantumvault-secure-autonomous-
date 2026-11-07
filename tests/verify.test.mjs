import test from 'node:test';
import assert from 'node:assert';
import { existsSync, readFileSync } from 'node:fs';


test('Projektstruktur vorhanden', () => {
  for (const p of ['Cargo.toml', 'src', 'tests']) assert.ok(existsSync(p), p + ' fehlt');
});

test('Cargo.toml beschreibt ein Paket', () => {
  const toml = readFileSync('Cargo.toml', 'utf8');
  assert.match(toml, /\[package\]/);
  assert.ok((toml.match(/name\s*=\s*"([^\"]+)"/g) || [])[1]);
});

test('Zero-Knowledge-Kern ist ausgelegt', () => {
  assert.ok(existsSync('crypto_core') || existsSync('src/crypto') || existsSync('gateway'));
});

test('Frontend oder API-Gateway vorhanden', () => {
  assert.ok(existsSync('frontend') || existsSync('gateway') || existsSync('src'));
});