function download() {
    var url = document.getElementById('url').value;
    var choice = document.getElementById('choice').value;
    var format = document.getElementById('format').value;

    // Additional validation logic if needed

    // Example: Check if the URL is not empty
    if (!url.trim()) {
        document.getElementById('errorMessage').innerHTML = 'Please enter a valid URL.';
        return;
    }

    // Check if the URL is valid
    var urlRegex = /^(https?:\/\/)?(www\.)?youtube\.com\/(watch\?v=|playlist\?list=|channel\/)[\w-]+$/;
    if (!urlRegex.test(url)) {
        document.getElementById('errorMessage').innerHTML = 'Please enter a valid YouTube URL.';
        return;
    }

    // Reset error and success messages
    document.getElementById('errorMessage').innerHTML = '';
    document.getElementById('successMessage').innerHTML = '';

    document.getElementById('loadingSpinner').style.display = 'block';

    var elementsToHide = document.getElementsByClassName("formElement");
    for (var i = 0; i < elementsToHide.length; i++){
        elementsToHide[i].style.display = "none";
    }

    // Generate a random parameter to avoid caching
    var randomParam = Math.random().toString(36).substring(7);

    // Fetch API request to the Flask endpoint with the random parameter
    fetch('/download?random=' + randomParam, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'url=' + encodeURIComponent(url) + '&choice=' + encodeURIComponent(choice) + '&format=' + encodeURIComponent(format),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loadingSpinner').style.display = 'none';

        if (data.status === 'success') {
            document.getElementById('successMessage').innerHTML = data.message;
            document.getElementById('successMessage').style.display='block'
        } else {
            document.getElementById('errorMessage').innerHTML = "Error while downloading file";
            document.getElementById('errorMessage')   .style.display='block'
        }

        // Call the additional function after downloading the video
        afterDownload();
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('loadingSpinner').style.display = 'none';
        document.getElementById('errorMessage').innerHTML = 'An error occurred.';
        document.getElementById('errorMessage').style.display='block';
        afterDownload();
    });
}

function afterDownload() {
    setTimeout(function() {
        var elementsToHide = document.getElementsByClassName("formElement");
        for (var i = 0; i < elementsToHide.length; i++){
            elementsToHide[i].style.display = "block";
        }
        document.getElementById('errorMessage').style.display='none';
        document.getElementById('successMessage').style.display='none';
        document.getElementById('url').value = ' ';

        location.reload();
    }, 4000);
}
