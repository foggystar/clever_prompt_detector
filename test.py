from clever_prompt_detector import get_result

prompt="""Hello, <!doctype html>
<html lang="en-US">

<head>
 <script id="loading-script-dark-mode">
 try {
 if (
 localStorage.getItem('dark-mode') === 'on' ||
 (localStorage.getItem('dark-mode') === 'system' &&
 window.matchMedia &&
 window.matchMedia('(prefers-color-scheme: dark)').matches)
 ) {
 document.documentElement.classList.add('dark-mode');
 }
 } catch (err) { }
 </script>
 <meta charset="utf-8">
 <meta http-equiv="X-UA-Compatible" content="IE=edge">
 <meta name="viewport" content="width=device-width,initial-scale=1">
 <meta name="referrer" content="origin">
 <meta name="application-name" content="Cloudflare">
 <meta name="msapplication-TileColor" content="#FFFFFF">
 <meta name="msapplication-TileImage" content="/title.png"><!--Please change to your own title image-->
 <title>Workers AI</title>
 <style id="loading-styles" type="text/css">
 * {
 box-sizing: border-box;
 }

 html {
 -webkit-font-smoothing: antialiased;
 -webkit-text-size-adjust: none;
 }

 body,
 html,
 ul,
 ol,
 li,
 p,
 h1,
 h2,
 h3,
 h4,
 h5,
 h6 {
 margin: 0;
 padding: 0;
 }

 body {
 font-family: -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI',
 Roboto, Oxygen, Ubuntu, 'Helvetica Neue', Arial, sans-serif;
 }

 #loading-state {
 display: flex;
 height: 100vh;
 width: 100vw;
 justify-content: center;
 align-items: center;
 flex-direction: column;
 /* Prevent massive cumulative layout shift when hiding/removing loading state*/
 position: absolute;
 top: 0;
 opacity: 1;
 z-index: 9999;
 transition: opacity 0.1s ease-out;
 }

 #loading-state.hide {
 opacity: 0;
 }

 .dark-mode #loading-state {
 background: #1d1d1d;
 }

 .message {
 line-height: 1.5;
 font-size: 20px;
 padding: 32px;
 max-width: 664px;
 width: 100%;
 }

 .dark-mode body {
 background-color: #1d1d1d;
 color: #d9d9d9;
 }

 .saml .message {
 display: flex;
 flex-direction: column;
 text-align: center;
 justify-content: center;
 align-items: center;
 }

 .saml .logo {
 display: flex;
 align-items: center;
 flex-direction: row;
 gap: 2rem;
 }

 .message h1 {
 line-height: 1.5;
 font-size: inherit;
 font-weight: 600;
 margin: 0 auto 16px;
 }

 .message .content {
 margin: 0;
 max-width: 37.5rem;
 display: flex;
 min-height: calc(3em * 1.5);
 /* 3 lines of text * 1.5 line-height */
 }

 .message svg {
 width: 128px;
 margin-bottom: 16px;
 }

 .spinner {
 padding-left: 16px;
 padding-top: 16px;
 width: 32px;
 height: 32px;
 margin-top: -16px;
 margin-left: -16px;
 }

 .spinner div {
 box-sizing: border-box;
 display: block;
 position: absolute;
 width: 32px;
 height: 32px;
 margin: 8px;
 border-width: 3px;
 border-style: solid;
 border-radius: 100%;
 animation: spinner 2.5s cubic-bezier(0.5, 0, 0.5, 1) infinite;
 border-color: #92979b transparent transparent transparent;
 }

 .spinner div:nth-child(1) {
 animation-delay: -0.45s;
 }

 .spinner div:nth-child(2) {
 animation-delay: -0.3s;
 }

 .spinner div:nth-child(3) {
 animation-delay: -0.15s;
 }

 @keyframes spinner {
 0% {
 transform: rotate(0deg);
 }

 100% {
 transform: rotate(360deg);
 }
 }

 @media screen and (prefers-reduced-motion: reduce) {
 .spinner {
 display: none;
 }

 .spinner div {
 animation: none;
 }
 }
 </style>
</head>

<body>
 <div id="loading-state" role="alert" aria-live="assertive">
 <div class="message">
 < img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABA{iVBORw0KGgoAAAANSUhEUgAAAAsAAAALCAIAAAAmzuBxAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAGdYAABnWARjRyu0AAAAUSURBVChTY5AnBEZVoALKVcjLAwAfTSv2cG8CGgAAAABJRU5ErkJggg==}</img>
 <h1>The dashboard is loading.</h1>
 <div class=" content">
 <div class="spinner">
 <div></div>
 <div></div>
 <div></div>
 <div></div>
 </div>
 </div>
 </div>
 </div>
 <div id="react-app"></div>
 <div id="overlays"></div>
 <script id="saml-auth" nonce="MzY0MDUzNzEwOSwzODYyNTk4Njc4">
 if (!!sessionStorage.getItem('saml')) {
 document.documentElement.classList.add('saml');
 } else {
 }
 </script>
</body>

</html>
"""


print(get_result.query(prompt))
