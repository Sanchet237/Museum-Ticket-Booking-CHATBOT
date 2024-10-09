// Selecting all payment method buttons and form sections
const methodCard = document.getElementById('method-card');
const methodBanking = document.getElementById('method-banking');
const methodGooglePay = document.getElementById('method-googlepay');
const methodUpi = document.getElementById('method-upi');

const cardSection = document.getElementById('card-section');
const bankingSection = document.getElementById('banking-section'); 
const googlePaySection = document.getElementById('googlepay-section'); 
const upiSection = document.getElementById('upi-section'); 

// Show the card payment section by default on page load
document.addEventListener('DOMContentLoaded', function() {
    showCardPayment();
});

// Show the card payment section
function showCardPayment() {
    displaySection('card-section');
}

// Show the banking payment section
function showBankingPayment() {
    displaySection('banking-section');
}

// Show the Google Pay payment section
function showGooglePayPayment() {
    displaySection('googlepay-section');
}

// Show the UPI payment section
function showUpiPayment() {
    displaySection('upi-section');
}

// Function to display a section and reset others
function displaySection(sectionId) {
    resetActiveSections();
    document.getElementById(sectionId).classList.add('active');
}

// Function to reset all sections and styles
function resetActiveSections() {
    const sections = ['card-section', 'banking-section', 'googlepay-section', 'upi-section'];
    sections.forEach(sectionId => {
        const section = document.getElementById(sectionId);
        if (section) section.classList.remove('active');
    });

    const methods = ['method-card', 'method-banking', 'method-googlepay', 'method-upi'];
    methods.forEach(methodId => {
        const method = document.getElementById(methodId);
        method.style.backgroundColor = '#34495e';
        method.style.color = '#ecf0f1';
    });
}

// Redirect to the selected bank's net banking page
function redirectToBank() {
    const bankSelect = document.getElementById('bank');
    const selectedBank = bankSelect.value;
    let bankUrl = '';

    switch (selectedBank) {
        case 'sbi':
            bankUrl = 'https://www.onlinesbi.com/';
            break;
        case 'axis':
            bankUrl = 'https://www.axisbank.com/';
            break;
        case 'hdfc':
            bankUrl = 'https://www.hdfcbank.com/';
            break;
        case 'icici':
            bankUrl = 'https://www.icicibank.com/';
            break;
        default:
            alert('Please select a valid bank.');
            return;
    }

    const email = document.getElementById('bank-email').value;
    if (email) {
        window.location.href = bankUrl;
    } else {
        alert('Please enter your email address.');
    }
}
