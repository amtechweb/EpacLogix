      // Function to set cookie and close the popup
    function acceptCookies() {
        // Set cookie expiration date to 1 year from now
        var expiryDate = new Date();
        expiryDate.setFullYear(expiryDate.getFullYear() + 1);
        // Set cookie value
        document.cookie = "cookies_accepted=true; expires=" + expiryDate.toUTCString() + "; path=/";
        // Hide the popup
        document.getElementById("cookie-popup").style.display = "none";
    }

    // Function to decline cookies and close the popup
    function declineCookies() {
        // Set cookie value to decline
        document.cookie = "cookies_accepted=false; path=/";
        // Hide the popup
        document.getElementById("cookie-popup").style.display = "none";
    }

    // Function to show cookie details modal
    function showCookieDetails() {
        document.getElementById("cookie-details-modal").style.display = "block";
    }

    // Function to close cookie details modal
    function closeCookieDetailsModal() {
        document.getElementById("cookie-details-modal").style.display = "none";
    }

    // Check if the cookies have been accepted
    window.onload = function() {
        var cookiesAccepted = getCookie("cookies_accepted");
        if (!cookiesAccepted) {
            document.getElementById("cookie-popup").style.display = "block";
        }
    };

    // Function to get cookie value by name
    function getCookie(name) {
        var cookieArr = document.cookie.split("; ");
        for (var i = 0; i < cookieArr.length; i++) {
            var cookiePair = cookieArr[i].split("=");
            if (name === cookiePair[0]) {
                return cookiePair[1];
            }
        }
        return null;
    }
