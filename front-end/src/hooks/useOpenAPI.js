import { useState, useEffect } from "react";

const useOpenAPI = (url) => {
  const [openAPI, setOpenAPI] = useState({});

  useEffect(() => {
    fetch(url)
      .then((response) => response.json())
      .then((data) => setOpenAPI(data));
  }, [url]);

  return openAPI;
};

export default useOpenAPI;
