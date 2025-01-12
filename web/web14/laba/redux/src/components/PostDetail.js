import React from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';

function PostDetail() {
  const { id } = useParams();
  const posts = useSelector((state) => state.posts);
  const post = posts[id];

  if (!post) {
    return <div>Пост не найден</div>;
  }

  return (
    <div>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
      <span>{post.date}</span>
    </div>
  );
}

export default PostDetail;
