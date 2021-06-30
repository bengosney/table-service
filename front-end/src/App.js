import CategoryList from "./components/categoryList";
import { initializeIcons } from '@fluentui/font-icons-mdl2';
initializeIcons();

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
