<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Camera Access</title>
</head>
<body>
    <h2>Access Camera</h2>
    <video id="video" width="640" height="480" autoplay></video>
    <button id="startBtn">Start Camera</button>
    <button id="captureBtn">Capture Image</button>
    <canvas id="canvas" style="display:none;"></canvas>
    <img id="grayscaleImage" style="max-width: 640px;"/>

    <script>
        const video = document.getElementById('video');
        const startBtn = document.getElementById('startBtn');
        const captureBtn = document.getElementById('captureBtn');
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const grayscaleImage = document.getElementById('grayscaleImage');

        // Start the camera when the button is clicked
        startBtn.addEventListener('click', async () => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                video.srcObject = stream;
            } catch (err) {
                console.error('Error accessing camera: ', err);
            }
        });

        // Capture the image when the button is clicked
        captureBtn.addEventListener('click', () => {
            // Draw the current frame from video to canvas
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            
            // Convert the canvas image to base64
            const imageData = canvas.toDataURL('image/png');
            
            // Send the captured image to the Flask server
            fetch('/api/image_processing', {   // Note the change here
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ image: imageData }),
            })
            .then(response => response.json())
            .then(data => {
                // Display the grayscale image received from the backend
                grayscaleImage.src = data.grayscale_image;
            })
            .catch(err => console.error('Error processing image:', err));
        });
    </script>
</body>
</html>
