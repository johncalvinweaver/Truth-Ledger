import hashlib
import time
import json
from typing import List

class LedgerEntry:
    def __init__(self, claim: str):
        self.claim = claim
        self.timestamp = self.generate_timestamp()
        self.hash = self.generate_hash()

    def generate_timestamp(self):
        return time.time()

    def generate_hash(self):
        entry_string = f"{self.claim}{self.timestamp}"
        return hashlib.sha256(entry_string.encode()).hexdigest()

    def to_dict(self):
        return {
            "claim": self.claim,
            "timestamp": self.timestamp,
            "hash": self.hash
        }

    def __repr__(self):
        return f"LedgerEntry(claim={self.claim}, timestamp={self.timestamp}, hash={self.hash})"

class Ledger:
    def __init__(self):
        self.entries: List[LedgerEntry] = []

    def add_entry(self, claim: str):
        entry = LedgerEntry(claim)
        self.entries.append(entry)
        self.save_ledger()
        return entry

    def save_ledger(self):
        with open('ledger.json', 'w') as f:
            json.dump([e.to_dict() for e in self.entries], f, indent=2)

    def load_ledger(self):
        try:
            with open('ledger.json', 'r') as f:
                data = json.load(f)
                self.entries = [LedgerEntry(d["claim"]) for d in data]
        except FileNotFoundError:
            self.entries = []

    def __repr__(self):
        return f"Ledger(entries={self.entries})"