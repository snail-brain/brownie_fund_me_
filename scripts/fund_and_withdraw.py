from brownie import FundMe
from scripts.helpful_scripts import getAccount

fund_me = FundMe[-1]
account = getAccount()


def fund_me():
    fund_me = FundMe[-1]
    account = getAccount()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = getAccount()
    fund_me.withdraw({"from": account})


def main():
    fund_me()
    withdraw()
