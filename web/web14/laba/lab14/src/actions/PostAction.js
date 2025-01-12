import { Dispatcher } from 'flux';

const dispatcher = new Dispatcher();

export const createPost = (title, content) => {
  dispatcher.dispatch({
    type: 'CREATE_POST',
    payload: { title, content, date: new Date().toLocaleString() }
  });
};

export const deletePost = (index) => {
  dispatcher.dispatch({
    type: 'DELETE_POST',
    payload: index
  });
};

export default dispatcher;
