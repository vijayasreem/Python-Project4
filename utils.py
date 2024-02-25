import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Other imports and functions remain the same

def send_password_reset_email(email: str, reset_link: str) -> None:
    """
    Send a password reset email to the user
    """
    msg = MIMEMultipart()
    msg['From'] = 'noreply@yourwebsite.com'
    msg['To'] = email
    msg['Subject'] = 'Password Reset Request'
    body = f'You have requested a password reset. Click the following link to reset your password: {reset_link}'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'your-password')
    server.send_message(msg)
    server.quit()

def reset_password_flow(account_number: str, email: str) -> None:
    """
    Handle the password reset flow
    """
    # Check if the account number and email match
    # This is a placeholder, replace with your actual logic
    if account_number == '123456' and email == 'user@example.com':
        # Generate a password reset link
        # This is a placeholder, replace with your actual logic
        reset_link = 'https://yourwebsite.com/reset_password?token=abcdef'
        send_password_reset_email(email, reset_link)

def is_valid_password(password: str) -> bool:
    if len(password) < MIN_PASSWORD_LEN:
        print("Password's length should be at least 8 characters!!!")
        return False

    if len(password) > MAX_PASSWORD_LEN:
        print("Password's length should be smaller or equal than 100 characters!!!")
        return False

    have_number, have_lowercase, have_uppercase, have_specical_character = False, False, False, False
    for char in password:
        if char == " ":
            return False
        if char.isnumeric():
            have_number = True
        elif char.islower():
            have_lowercase = True
        elif char.isupper():
            have_uppercase = True
        elif char in string.punctuation:
            have_specical_character = True

    if not (have_number and have_lowercase and have_uppercase and have_specical_character):
        print("Password must contain at least one number, one lowercase letter, one uppercase letter, and one special character!!!")
        return False

    return True

# Other functions remain the same
