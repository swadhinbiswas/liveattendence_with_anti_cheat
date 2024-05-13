import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';

export default function ImageAvatars() {
  return (
    <Stack direction="row" spacing={2}>
      <Avatar alt="Swadhin" src="https://avatars.githubusercontent.com/u/144092840?v=4" />
      <Avatar alt="Tuhin" src="https://avatars.githubusercontent.com/u/159527403?v=4" />
      <Avatar alt="Cindy Baker" src="https://raw.githubusercontent.com/swadhinbiswas/liveattendence_with_anti_cheat/main/photos/Screenshot%20from%202024-05-14%2001-11-30.png" />
    </Stack>
  );
}
