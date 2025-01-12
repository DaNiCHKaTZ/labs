import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createPost } from '../actions/PostAction.js';

function PostForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title && content) {
      createPost(title, content);
      setTitle('');
      setContent('');
      navigate('/');
    } else {
      alert('Пожалуйста, заполните все поля.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Название"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Текст"
        value={content}
        onChange={(e) => setContent(e.target.value)}
      ></textarea>
      <button type="submit">Добавить пост</button>
    </form>
  );
}

export default PostForm;
