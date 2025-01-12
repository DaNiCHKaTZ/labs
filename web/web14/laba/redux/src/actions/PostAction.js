export const CREATE_POST = 'CREATE_POST';
export const DELETE_POST = 'DELETE_POST';

export const createPost = (title, content) => ({
  type: CREATE_POST,
  payload: { title, content, date: new Date().toLocaleString() }
});

export const deletePost = (index) => ({
  type: DELETE_POST,
  payload: index
});
