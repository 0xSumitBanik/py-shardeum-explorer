import pytest
from shardeumexplorer import ShardeumExplorer

FIRST_TEST_ADDRESS = "0x822429119D53055fB11E69213613851ba28bd888"

def test_get_account_balance(get_network):
  shardeum_explorer = ShardeumExplorer(get_network)
  balance = shardeum_explorer.get_account_balance(FIRST_TEST_ADDRESS)
  assert balance > 0.0

def test_total_accounts(get_network):
  shardeum_explorer = ShardeumExplorer(get_network)
  total_accounts = shardeum_explorer.total_accounts()
  assert total_accounts > 0
