def test_separate_paren_groups(separate_paren_groups):
    assert separate_paren_groups('(()()) ((())) () ((())()())') == [ '(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == [ '()', '(())', '((()))', '(((())))' ]
