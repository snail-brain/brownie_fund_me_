from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    Local_Blockchain_Environments,
    getAccount,
    deploy_mocks,
)
from web3 import Web3


def deploy_fund_me():
    account = getAccount()

    if network.show_active() not in Local_Blockchain_Environments:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    # pass the price feed address to our fundme contract

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
