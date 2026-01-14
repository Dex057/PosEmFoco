from dataclasses import dataclass, field
from typing import List

@dataclass
class Interesse:
    palavra_chave: str

@dataclass
class Usuario:
    nome: str
    email: str
    interesses: List[Interesse] = field(default_factory=list)

@dataclass
class Edital:
    titulo: str
    link: str = "" 