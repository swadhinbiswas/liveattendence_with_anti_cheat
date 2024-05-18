import React, { useEffect, useRef } from 'react';
import axios from 'axios';

const VideoFeed = () => {
  return (
    <div classname='video'>
      <h1 className="test">Video Feed</h1>
      <img  className="videofeeds" src="http://localhost:8000/video/video_feed" alt="Video Feed" />

      
      
    </div>
  );
};

export default VideoFeed;