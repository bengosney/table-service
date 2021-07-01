import CategoryList from "./components/categoryList";
import { Grommet, Header, Main, Text  } from "grommet";

function App() {
  return (
    <Grommet plain>
      <Main pad={'medium'}>
        <Header>Table Service</Header>
        <CategoryList />
      </Main>
    </Grommet>
  );
}

export default App;
