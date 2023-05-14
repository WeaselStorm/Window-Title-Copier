document.addEventListener('DOMContentLoaded', function () {
    var copyButton = document.getElementById('copyButton');

    copyButton.addEventListener('click', function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var title = tabs[0].title;
            copyToClipboard(title);
        });
    });

    function copyToClipboard(text) {
        navigator.clipboard.writeText(text)
            .then(function () {
                console.log('Copied to clipboard:', text);
                copyButton.innerHTML = 'Copied! <span class=\"checkmark\">&#10003;</span>';
                copyButton.classList.add('copied');
                setTimeout(function () {
                    copyButton.classList.remove('copied');
                    copyButton.innerHTML = "Copy Window Title";
                }, 1500);
            })
            .catch(function (error) {
                
                console.error('Unable to copy to clipboard:', error);
            });
    }
});
