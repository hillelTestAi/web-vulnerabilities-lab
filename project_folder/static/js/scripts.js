// ולידציות פשוטות כדי למנוע טעויות נפוצות

function validateSQLInput() {
    const input = document.querySelector('input[name="username"]').value;
    if (/['"=;]/.test(input)) {
        alert("אל תשתמש בתווים מסוכנים! נסה שוב.");
        return false;
    }
    return true;
}

function validateXSSInput() {
    const input = document.querySelector('input[name="comment"]').value;
    if (/script|<|>/.test(input.toLowerCase())) {
        alert("הכנסה של סקריפטים לא חוקית!");
        return false;
    }
    return true;
}

function validateParameterTampering() {
    const price = document.querySelector('input[name="price"]').value;
    if (isNaN(price) || price <= 0) {
        alert("מחיר לא חוקי! נסה שוב.");
        return false;
    }
    return true;
}
