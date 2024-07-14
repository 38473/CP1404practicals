def main():
    """This program is stores users' emails (unique keys) and names (values) in a dictionary
    and check if the name is correct, then output the emails and names"""
    emails = get_user_name_and_email()
    print_user_email_and_name(emails)


def get_user_name_and_email():
    """
    ask users for their name and stored in a dictionary
    """
    emails = {}
    email = input("Email: ").strip()
    while email != "":
        username = email.split('@')[0]
        parts = username.split('.')
        username = ' '.join(parts).title()
        check_name = input(f"Is your name {username}? (Y/n) ").strip().lower()
        if check_name in ('', 'y', 'yes'):
            name = username.title()
        else:
            name = input("Name: ").title()
        emails[email] = name
        email = input("Email: ").strip()
    return emails


def print_user_email_and_name(emails):
    """
    Print users name and email from the dictionary.
    """
    for email, name in emails.items():
        print(f"{name} ({email})")


main()