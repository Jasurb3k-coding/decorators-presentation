from enum import Enum
from dataclasses import dataclass


class Codes(Enum):
    PAID_IN_FULL = "paid_in_full"
    PAID_IN_PART = "paid_in_part"
    DECLARED_BANKRUPTCY = "declared_bankruptcy"
    SAVING_FAILED = 'saving_failed'


@dataclass
class StatusUpdate:
    user_id: str
    loan_id: str
    code: Codes


@dataclass
class PaidInFull(StatusUpdate):
    code: Codes = Codes.PAID_IN_FULL


@dataclass
class PaidInPart(StatusUpdate):
    code: Codes = Codes.PAID_IN_PART


@dataclass
class DeclaredBankruptcy(StatusUpdate):
    code: Codes = Codes.DECLARED_BANKRUPTCY


@dataclass
class SavingFailed(StatusUpdate):
    code: Codes = Codes.SAVING_FAILED
