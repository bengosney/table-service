import logo from './logo.svg';
import './App.css';
import ProductList from './components/productList';
import CategoryList from './components/categoryList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <CategoryList />
      </header>
    </div>
  );
}

export default App;
