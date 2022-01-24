from dataclasses import dataclass

@dataclass
class Transaction:
	id: str #shouldnt be a string but i have to research that later
	amount: int
	payee: str #question is if we want 
	account: str # there should be an also some kind of account dataclass

