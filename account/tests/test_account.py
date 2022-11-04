from account.account import Account


class TestAccount:
    def test_create_account(self):
        new_account = Account(
            1,
            'Ian',
            0
        )
        assert new_account.id == 1
        assert new_account.name == 'Ian'
        assert new_account.balance == 0
        
