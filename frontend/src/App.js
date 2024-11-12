import { ToastContainer } from 'react-toastify';
import './App.css';
import SearchView from './views/SearchView';

function App() {
  return (
    <div className="content">
        <SearchView/>
        <ToastContainer />
    </div>
  );
}

export default App;
