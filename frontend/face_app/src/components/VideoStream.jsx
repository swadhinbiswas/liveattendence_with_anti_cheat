import React, { useState, useEffect } from 'react';

const VideoStream = () => {
  const [src, setSrc] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchVideoStream = async () => {
      try {
        const response = await fetch('http://localhost:8000/video/video_feed'); // Replace with your actual URL
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const reader = response.body.getReader();
        const pump = async () => {
          const { done, value } = await reader.read();
          if (done) {
            return;
          }
          // Process the received video data
          try {
            const separator = value.indexOf('\r\n\r\n')
            const frameData = value.slice(separator + 4);  // Extract frame data
            const blob = new Blob([frameData], { type: 'image/jpeg' });
            setSrc(URL.createObjectURL(blob));
          } catch (error) {
            console.error('Error processing video frame:', error);
            setError(error); // Set error state for handling
          }
          pump();
        };
        pump();
      } catch (error) {
        console.error('Error fetching video stream:', error);
        setError(error); // Set error state for handling
      }
    };

    fetchVideoStream();
  }, []); // Fetch on component mount

  return (
    <div>
      {error ? (
        <p>Error: {error.message}</p>
      ) : src ? (
        <video src={src} autoPlay controls />
      ) : (
        <p>Loading video stream...</p>
      )}
    </div>
  );
};

export default VideoStream;