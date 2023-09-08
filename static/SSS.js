window.addEventListener("load", function() {
    document.querySelector("#loader").style.display = "none";
  });

  function menu_bar(){
    document.getElementById("menu").style.visibility ="visible";
    document.getElementById("Closer").style.visibility = "visible";
}
function close_button(){
    document.getElementById("menu").style.visibility ="hidden";
    document.getElementById("Closer").style.visibility = "hidden";
}

function Content(){
  document.getElementById("Content_PopUp").style.visibility = "Visible";
}
function PB(){
  document.getElementById("Content_PopUp").style.visibility = "hidden";
}
function About(){
  document.querySelector("#About_SEction").style.visibility = "Visible";
  document.querySelector("#Aboutxyz").style.visibility = "hidden";
}

document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('thumbnail');
    const imagePreview = document.getElementById('content-preview');
    fileInput.addEventListener('change', () => {
    	const file = fileInput.files[0];
    	const reader = new FileReader()
    	reader.addEventListener('load', () => {
    		const imageUrl = reader.result;
    		const image = new Image();
    		image.src = imageUrl;
    		imagePreview.innerHTML = '';
    		imagePreview.appendChild(image);

            document.getElementById("content-preview").style.visibility = "visible";
    	});

    	if (file) {
    		reader.readAsDataURL(file);
    	}
    });
});

document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('Video');
  const videoPreview = document.getElementById('V-content');

  fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    const video = document.createElement('video');
    video.controls = true;
    videoPreview.innerHTML = '';
    videoPreview.appendChild(video);
    document.getElementById("V-content").style.visibility = "visible";
    document.getElementById("video").style.zIndex = 0;

    const reader = new FileReader();
    reader.addEventListener('load', () => {
      video.src = reader.result;
    });

    if (file) {
      reader.readAsDataURL(file);
    }
  });

});

function changeBackground() {
  var trailerInput = document.getElementById("Trailer");
  var trailerC = document.getElementById("TrailerC");
  
  if (trailerInput.files.length > 0) {
    trailerC.style.backgroundColor = "green";
    document.getElementById("TrailerPW").style.color= 'green';
    document.getElementById("TrailerPW").style.height= '0';
    document.getElementById("TrailerW").style.height="auto";
  }
}


document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('image');
    const imagePreview = document.getElementById('content-preview');
    fileInput.addEventListener('change', () => {
    	const file = fileInput.files[0];
    	const reader = new FileReader()
    	reader.addEventListener('load', () => {
    		const imageUrl = reader.result;
    		const image = new Image();
    		image.src = imageUrl;
    		imagePreview.innerHTML = '';
    		imagePreview.appendChild(image);

            document.getElementById("content-preview").style.visibility = "visible";
    	});

    	if (file) {
    		reader.readAsDataURL(file);
    	}
    });
});

document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('pAdd');
  const imagePreview = document.getElementById('Pphoto');
  fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    const reader = new FileReader()
    reader.addEventListener('load', () => {
      const imageUrl = reader.result;
      const image = new Image();
      image.src = imageUrl;
      imagePreview.innerHTML = '';
      imagePreview.appendChild(image);

          document.getElementById("pAdd").style.visibility = "hidden";
          document.getElementById("PAddl").style.visibility = "hidden";
          document.getElementById("ProfilePhotoS").style.visibility = "Visible";
    });

    if (file) {
      reader.readAsDataURL(file);
    }
  });
});


document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('short');
    const videoPreview = document.getElementById('V-content');

    fileInput.addEventListener('change', () => {
      const file = fileInput.files[0];
      const video = document.createElement('video');
      video.controls = true;
      videoPreview.innerHTML = '';
      videoPreview.appendChild(video);
      document.getElementById("V-content").style.visibility = "visible";

      const reader = new FileReader();
      reader.addEventListener('load', () => {
        video.src = reader.result;
      });

      if (file) {
        reader.readAsDataURL(file);
      }
    });
 
});

document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('thum');
    const imagePreview = document.getElementById('content-preview');
    fileInput.addEventListener('change', () => {
    	const file = fileInput.files[0];
    	const reader = new FileReader()
    	reader.addEventListener('load', () => {
    		const imageUrl = reader.result;
    		const image = new Image();
    		image.src = imageUrl;
    		imagePreview.innerHTML = '';
    		imagePreview.appendChild(image);

            document.getElementById("content-preview").style.visibility = "visible";
    	});

    	if (file) {
    		reader.readAsDataURL(file);
    	}
    });
});


function share() {
  document.getElementById("ShereCloser").style.visibility = "Visible";
  document.getElementById("shereOptions").style.visibility = "Visible";
}

function ShereCloser(){
  document.getElementById("ShereCloser").style.visibility = "hidden";
  document.getElementById("shereOptions").style.visibility = "hidden";
  document.getElementById("commentTTT").style.visibility = "hidden"; 
  document.getElementById("Description").style.visibility = "hidden";
}

function shareOnFacebook() {
  var url = "https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(window.location.href);
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnTwitter() {
  var url = "https://twitter.com/intent/tweet?text=" + encodeURIComponent(document.title) + "&url=" + encodeURIComponent(window.location.href);
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function openInstagramProfile(username) {
  var url = "https://www.instagram.com/" + username;
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}


function shareOnLinkedIn() {
  var url = "https://www.linkedin.com/sharing/share-offsite/?url=" + encodeURIComponent(window.location.href);
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnPinterest() {
  var url = "https://www.pinterest.com/pin/create/button/?url=" + encodeURIComponent(window.location.href) + "&media=" + encodeURIComponent(document.querySelector('meta[property="og:image"]').getAttribute('content')) + "&description=" + encodeURIComponent(document.querySelector('meta[property="og:description"]').getAttribute('content'));
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnWhatsApp() {
  var url = "https://wa.me/?text=" + encodeURIComponent(document.title + " " + window.location.href);
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnShareChat() {
  var url = "https://sharechat.com/profile/your_username_here/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}
function shareOnDiscord() {
  var url = "https://discord.gg/your_invite_link_here";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnWeChat() {
  // Replace this URL with your actual WeChat QR code URL
  var url = "https://example.com/your_wechat_qr_code.png"; 
  window.open(url, "_blank");
}

function shareOnTumblr() {
  var url = "https://www.tumblr.com/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnVimeo() {
  var url = "https://vimeo.com/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnReddit() {
  var url = "https://www.reddit.com/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnTwitch() {
  var url = "https://www.twitch.tv/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}
function shareOnQuora() {
  var url = "https://www.quora.com/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}
 
function shareOnWeibo() {
  var url = "https://weibo.com/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function shareOnVK() {
  var url = "https://vk.com/";
  var link = document.createElement('a');
  link.setAttribute('target', '_blank');
  link.setAttribute('href', url);
  link.click();
}

function Commentt(){
  document.getElementById("ShereCloser").style.visibility = "Visible";
  document.getElementById("commentTTT").style.visibility = "Visible";
}

function Shere(){
  document.getElementById("ShereCloser").style.visibility = "Visible";
  document.getElementById("shereOptions").style.visibility = "Visible";
}


document.addEventListener('DOMContentLoaded', function() {
  var element = document.getElementById('HistoryContainer');

  if (element) {
    element.addEventListener('click', function() {
      // your event listener code here
      document.getElementById("HistoryContainer").style.height = "5cm";
    });
  }
});



document.addEventListener("DOMContentLoaded", function() {
  const historyContainer = document.getElementById("HistoryContainer");

  historyContainer.addEventListener("mouseleave", function() {
    console.log("Mouse pointer has left the HistoryContainer div.");
    // Add your code here to handle the mouseleave event.
    document.getElementById("HistoryContainer").style.height = "1cm";
  });
});


function VHistory(){
  document.getElementById('Video').style.visibility="visible";
  document.getElementById('Image').style.visibility="hidden";
  document.getElementById('ImageH').style.visibility ="hidden";
  document.getElementById('MiniH').style.visibility = "hidden";
  document.getElementById("VideoH").style.visibility ="visible";
  document.getElementById('Mini').style.visibility="hidden";
  document.getElementById('Announcement').style.visibility="hidden";
  document.getElementById("AnuH").style.visibility = "hidden";
}

function IHistory(){
  document.getElementById('Video').style.visibility="hidden";
  document.getElementById('Image').style.visibility="visible";
  document.getElementById('ImageH').style.visibility ="visible";
  document.getElementById('MiniH').style.visibility = "hidden";
  document.getElementById("VideoH").style.visibility ="hidden";
  document.getElementById('Mini').style.visibility="hidden";
  document.getElementById('Announcement').style.visibility="hidden";
  document.getElementById("AnuH").style.visibility = "hidden";
}

function MHistory(){
  document.getElementById('Video').style.visibility="hidden";
  document.getElementById('Image').style.visibility="hidden";
  document.getElementById('ImageH').style.visibility ="hidden";
  document.getElementById('MiniH').style.visibility = "visible";
  document.getElementById("VideoH").style.visibility ="hidden";
  document.getElementById('Mini').style.visibility="visible";
  document.getElementById('Announcement').style.visibility="hidden";
  document.getElementById("AnuH").style.visibility = "hidden";
}

function AHistory(){
  document.getElementById('Video').style.visibility="hidden";
  document.getElementById('Image').style.visibility="hidden";
  document.getElementById('Mini').style.visibility="hidden";
  document.getElementById('Announcement').style.visibility="visible";
  document.getElementById('ImageH').style.visibility ="hidden";
  document.getElementById('MiniH').style.visibility = "hidden";
  document.getElementById("VideoH").style.visibility ="hidden";
  document.getElementById("AnuH").style.visibility = "visible";
}

function VeHistory(){
  document.getElementById('LIKEDVIDEO').style.visibility="visible";
  document.getElementById('LIKEDIMAGE').style.visibility="hidden";
  document.getElementById('LIKEDMINI').style.visibility ="hidden";
  document.getElementById('LIKEDANU').style.visibility = "hidden";
  document.getElementById("LVideo").style.visibility ="visible";
  document.getElementById('LImage').style.visibility="hidden";
  document.getElementById('LAnnouncement').style.visibility="hidden";
  document.getElementById("LMini").style.visibility = "hidden";
}

function ImHistory(){
  document.getElementById('LIKEDVIDEO').style.visibility="hidden";
  document.getElementById('LImage').style.visibility="visible";
  document.getElementById('LIKEDIMAGE').style.visibility ="visible";
  document.getElementById('LIKEDMINI').style.visibility = "hidden";
  document.getElementById("LVideo").style.visibility ="hidden";
  document.getElementById('LMini').style.visibility="hidden";
  document.getElementById('LAnnouncement').style.visibility="hidden";
  document.getElementById("LIKEDANU").style.visibility = "hidden";
}

function MiHistory(){
  document.getElementById('LIKEDVIDEO').style.visibility="hidden";
  document.getElementById('LImage').style.visibility="hidden";
  document.getElementById('LIKEDIMAGE').style.visibility ="hidden";
  document.getElementById('LIKEDMINI').style.visibility = "visible";
  document.getElementById("LVideo").style.visibility ="hidden";
  document.getElementById('LMini').style.visibility="visible";
  document.getElementById('LAnnouncement').style.visibility="hidden";
  document.getElementById("LIKEDANU").style.visibility = "hidden";
}

function AnHistory(){
  document.getElementById('LIKEDVIDEO').style.visibility="hidden";
  document.getElementById('LImage').style.visibility="hidden";
  document.getElementById('LMini').style.visibility="hidden";
  document.getElementById('LAnnouncement').style.visibility="visible";
  document.getElementById('LIKEDIMAGE').style.visibility ="hidden";
  document.getElementById('LIKEDMINI').style.visibility = "hidden";
  document.getElementById("LVideo").style.visibility ="hidden";
  document.getElementById("LIKEDANU").style.visibility = "visible";
}
function options(){
  document.getElementById("Options").style.visibility="visible";
  document.getElementById("optionCloser").style.visibility="visible";
  document.getElementById("Opener").style.visibility="hidden";
}
function optionCloser(){
  document.getElementById("Options").style.visibility="hidden";
  document.getElementById("optionCloser").style.visibility="hidden";
  document.getElementById("Opener").style.visibility="visible";
}
const searchInput = document.getElementById("searchInput");
const suggestionList = document.getElementById("suggestionList");

searchInput.addEventListener("input", handleInput);

function handleInput() {
  const inputText = searchInput.value.trim();
  
  // Clear previous suggestions
  suggestionList.innerHTML = "";

  if (inputText !== "") {
    // Send a request to fetch suggestions from the server or use predefined suggestions
    const suggestions = getSuggestions(inputText);

    suggestions.forEach(suggestion => {
      const suggestionItem = document.createElement("li");
      suggestionItem.classList.add("suggestionItem");
      suggestionItem.textContent = suggestion;
      suggestionItem.addEventListener("click", () => {
        // Handle suggestion selection
        handleSuggestionSelection(suggestion);
      });
      suggestionList.appendChild(suggestionItem);
    });
  }
}

function getSuggestions(inputText) {
  // Replace this with your server-side logic or predefined suggestions
  const predefinedSuggestions = ["Apple", "Banana", "Orange", "Pineapple", "Watermelon"];
  
  // Filter suggestions based on input
  const filteredSuggestions = predefinedSuggestions.filter(suggestion =>
    suggestion.toLowerCase().includes(inputText.toLowerCase())
  );

  return filteredSuggestions;
}

function handleSuggestionSelection(suggestion) {
  searchInput.value = suggestion;
  // Handle further actions (e.g., submitting the form)
}

function Searchengager(){
  document.getElementById("Searchinterface").style.visibility= "visible";
}
function SearchCloser(){
  document.getElementById("Searchinterface").style.visibility= "hidden";
}


// Ajax coding
function updateOptions(responseData) {
  // Create a temporary div element to hold the response HTML
  var tempDiv = document.createElement('div');
  tempDiv.innerHTML = responseData;

  // Extract the specific portion of the HTML using selectors or other methods
  var updatedOptionsHTML = tempDiv.querySelector('#Options').innerHTML;

  // Update the specific portion of the webpage
  document.getElementById('Options').innerHTML = updatedOptionsHTML;
}
function LIkeUpgrade(){
  //input of the name of the content
  var cont = document.getElementById("likeforjs").value;
  let c = encodeURIComponent(cont);
  console.log(cont);
  console.log("js is working");
  const xhr = new XMLHttpRequest();
    xhr.open('GET','/Like?Content='+ c,  true);
    xhr.onload = function(){
      //for cheaking status
      if(this.status === 200){
        var updatedContent = xhr.responseText;
        updateOptions(updatedContent);
      }
      else{
          console.log("Some error occured");
      }
    }
  xhr.send();
}


/*
    function updateComment(responseData) {
  if (responseData) {
    // Create a temporary div element to hold the response HTML
    var tempDiv = document.createElement('div');
    tempDiv.innerHTML = responseData;

    // Check if the target element exists in the response HTML
    var updatedCommentsElement = tempDiv.querySelector('.CommentCollector');
    if (updatedCommentsElement) {
      // Extract the HTML content from the target element
      var updatedCommentsHTML = updatedCommentsElement.innerHTML;

      // Update the specific portion of the webpage
      var currentCommentsElement = document.querySelector('.CommentCollector');
      if (currentCommentsElement) {
        currentCommentsElement.innerHTML = updatedCommentsHTML;
      } else {
        console.error("Current .CommentCollector element not found.");
      }
    } else {
      console.error(".CommentCollector element not found in response HTML.");
    }
  } else {
    console.error("Response data is null.");
  }
}

function postFormData() {
  var formData = new FormData();
  formData.append("Comment", document.getElementById("ComCom").value);

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/Community', true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      var response = xhr.responseText;
      updateComment(response);
      var inputElement = document.getElementById("ComCom");
      inputElement.value = "";
    } else {
      console.log("Some error occurred");
    }
  };
  xhr.send(formData);
}
*/