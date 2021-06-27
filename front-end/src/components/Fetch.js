import React from "react";

import useFetch from "../hooks/useFetch";
import Loader from "./loader";

const Fetch = ({ url, children }) => {
  const [data, loading, error] = useFetch(url);

  if (error !== null) {
    return <pre>{error}</pre>;
  }

  return (
    <Loader loading={loading}>
      {React.cloneElement(children, { data: data })}
    </Loader>
  );
};

export default Fetch;
