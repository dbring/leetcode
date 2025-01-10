class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        TC: O(mnlogmn), SC: O(mn) where m = len(accounts), n is the maximum length
        of an account
        """
        account_graph = {}
        email_to_name = {}
        merged_accounts = []

        for account in accounts:
            name = account[0]
            email_head = account[1]

            for i in range(1, len(account)):
                current_email = account[i]

                if email_head not in account_graph:
                    account_graph[email_head] = set()

                account_graph[email_head].add(current_email)

                if current_email not in account_graph:
                    account_graph[current_email] = set()

                account_graph[current_email].add(email_head)

                email_to_name[current_email] = name

        def dfs(current_email, merged_account):
            if current_email in visited:
                return

            visited.add(current_email)
            merged_account.append(current_email)

            for neighbor in account_graph[current_email]:
                dfs(neighbor, merged_account)

            return merged_account

        visited = set()
        for email in email_to_name:
            if email in visited:
                continue

            merged_account = dfs(email, [])
            merged_accounts.append([email_to_name[email]] + sorted(merged_account))

        return merged_accounts
