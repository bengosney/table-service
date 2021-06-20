import useOpenAPI from "./useOpenAPI";

import { useEffect, useState } from "react";

const useGroupedSchemas = (url) => {
  const openAPI = useOpenAPI(url);
  const [groupedSchemas, setGroupedSchemas] = useState({});

  useEffect(() => {
    const { components: { schemas = {} } = {} } = openAPI;

    if (schemas.length != 0) {
      const grouped_schemas = Object.keys(schemas).reduce((groups, key) => {
        const parts = key.split("_");
        const type = parts[1] || "details";
        const name = parts[0];
        groups[name] = groups[name] || {};
        groups[name][type.toLowerCase()] = schemas[key];
        return groups;
      }, {});

      setGroupedSchemas(grouped_schemas);
    }
  }, [openAPI]);

  return groupedSchemas;
};

export default useGroupedSchemas;
