import streamlit as st

# Initialize session state for account storage
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

# Function to create a new account
def create_account(account_number, name, balance):
    if account_number not in st.session_state.accounts:
        st.session_state.accounts[account_number] = {"name": name, "balance": balance}
        return "Account created successfully."
    else:
        return "Account already exists."

# Function to validate account existence
def account_exists(account_number):
    return account_number in st.session_state.accounts

# Function to deposit money
def deposit(account_number, amount):
    if account_exists(account_number):
        st.session_state.accounts[account_number]["balance"] += amount
        return f"Deposited {amount} successfully."
    else:
        return "Account not found."

# Function to withdraw money
def withdraw(account_number, amount):
    if account_exists(account_number):
        if st.session_state.accounts[account_number]["balance"] >= amount:
            st.session_state.accounts[account_number]["balance"] -= amount
            return f"Withdrawn {amount} successfully."
        else:
            return "Insufficient balance."
    else:
        return "Account not found."

# Function to check balance
def check_balance(account_number):
    if account_exists(account_number):
        return f"Balance: {st.session_state.accounts[account_number]['balance']}"
    else:
        return "Account not found."

# Streamlit UI
st.title("Bank Management System")

menu = ["Create Account", "Deposit", "Withdraw", "Check Balance"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Create Account":
    account_number = st.text_input("Enter account number:")
    name = st.text_input("Enter account holder's name:")
    balance = st.number_input("Enter initial balance:", min_value=0.0, format="%.2f")
    if st.button("Create Account"):
        result = create_account(account_number, name, balance)
        st.success(result)

elif choice == "Deposit":
    account_number = st.text_input("Enter account number:")
    amount = st.number_input("Enter amount to deposit:", min_value=0.0, format="%.2f")
    if st.button("Deposit"):
        result = deposit(account_number, amount)
        st.success(result)

elif choice == "Withdraw":
    account_number = st.text_input("Enter account number:")
    amount = st.number_input("Enter amount to withdraw:", min_value=0.0, format="%.2f")
    if st.button("Withdraw"):
        result = withdraw(account_number, amount)
        st.success(result)

elif choice == "Check Balance":
    account_number = st.text_input("Enter account number:")
    if st.button("Check Balance"):
        result = check_balance(account_number)
        st.success(result)
