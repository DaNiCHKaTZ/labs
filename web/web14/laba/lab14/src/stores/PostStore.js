import { EventEmitter } from 'events';
import dispatcher from '../actions/PostAction.js';

class PostStore extends EventEmitter {
  constructor() {
    super();
    this.posts = [];
  }

  createPost(post) {
    this.posts.push(post);
    this.emit('change');
  }

  deletePost(index) {
    this.posts = this.posts.filter((_, i) => i !== index);
    this.emit('change');
  }

  getAllPosts() {
    return this.posts;
  }

  handleActions(action) {
    switch(action.type) {
      case 'CREATE_POST':
        this.createPost(action.payload);
        break;
      case 'DELETE_POST':
        this.deletePost(action.payload);
        break;
      default:
        break;
    }
  }
}

const postStore = new PostStore();
dispatcher.register(postStore.handleActions.bind(postStore));
export default postStore;
