import React from 'react'
import axios from 'axios';

const Adminpage = () => {
  const [selectedFile, setSelectedFile] = useState(null);
    const [id, setId] = useState('');
    const [formData, setFormData] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [uploadError, setUploadError] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleIdChange = (event) => {
        setId(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!selectedFile || !id) {
            setUploadError('Please select a photo and enter an ID.');
            return;
        }

        setIsLoading(true);
        setUploadError(null);

        const formData = new FormData();
        formData.append('photo', selectedFile);
        formData.append('id', id);

        try {
            const response = await axios.post('/your-backend-endpoint', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('Upload successful:', response.data);
            // Handle successful upload (e.g., display success message)
        } catch (error) {
            console.error('Upload failed:', error);
            setUploadError('Error uploading photo. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" accept="image/*" onChange={handleFileChange} />
            <label htmlFor="id">ID:</label>
            <input type="text" id="id" value={id} onChange={handleIdChange} />
            <button type="submit" disabled={isLoading}>
                {isLoading ? 'Uploading...' : 'Upload Photo and ID'}
            </button>
            {uploadError && <p className="error">{uploadError}</p>}
        </form>
    );
};

export default Adminpage