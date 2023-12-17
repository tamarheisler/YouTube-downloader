document.addEventListener('DOMContentLoaded', function () {
    var successMessage = document.getElementById('successMessage');
    if (window.location.href.indexOf("success") > -1) {
        successMessage.style.display = 'block';
    }
});

document.addEventListener('DOMContentLoaded', function () {
var urlInput = document.getElementById('url');
var choiceSelect = document.getElementById('choice');
var choiceLabel = document.getElementById('chicelabel');

// הסתר את ה-<select> בהתאם לתוכן של ה-<input>
function toggleSelectVisibility() {
    if (urlInput.value.toLowerCase().includes('youtube')) {
        choiceSelect.style.display = 'block'; // הצג את ה-<select>
        choiceLabel.style.display = 'block'; // הצג את ה-<select>
    } else {
        choiceSelect.style.display = 'none'; // הסתר את ה-<select>
        choiceLabel.style.display = 'none'; // הסתר את ה-<select>
    }
}

function updateEmbed() {
    // Get the value from the 'url' input field
    var urlInput = document.getElementById('url');
    var imageUrl = urlInput.value;

    // Update the 'src' attribute of the 'embed' element
    var embedElement = document.getElementById('vidPreview');
    embedElement.src = imageUrl;
}

// הפעל את הפונקציה גם כאשר משתנה ערך ב-<input>
urlInput.addEventListener('input', toggleSelectVisibility);
urlInput.addEventListener('input', updateEmbed);

// הסתר את ה-<select> בהתאם לערך ההתחלתי בטעינת העמוד
toggleSelectVisibility();
updateEmbed();
});

function submitClicked(){
    const url = document.getElementById('url').value;

    const form = document.getElementById('dForm');
    loading.style.display = 'block'
    form.style.display = 'none'
}



const showResponseMessage = (success, message) => {
    const container = $("#messageContainer");
    const content = $("#messageContent");
    const style = success ? "success" : "fail";

    container.addClass(`message-${style}`);
    content.text(message);
    container.show();

    setTimeout(() => {
        container.hide();
    }, 3000);
}
