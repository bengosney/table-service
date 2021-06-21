import { Switch, Route, useRouteMatch, useParams } from "react-router-dom";
import Form from "@rjsf/fluent-ui";
import useGroupedSchemas from "../hooks/useGroupedSchemas";

const SchemaForm = ({ ...props }) => {
  const { schematype } = useParams();
  const schemas = useGroupedSchemas();

  const typeSchemas =  schemas[schematype] || {};

  if (typeof typeSchemas.create == 'undefined') {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h2>{schematype}</h2>
      <Form schema={schemas[schematype].create} />
    </div>
  );
};

const Admin = ({ ...props }) => {
  const { path, url } = useRouteMatch();

  return (
    <div>
      <h1>Admin</h1>
      <Switch>
        <Route exact path={path}>
          <p>Select a thing</p>
        </Route>
        <Route path={`${path}:schematype`}>
          <SchemaForm />
        </Route>
      </Switch>
    </div>
  );
};

export default Admin;
