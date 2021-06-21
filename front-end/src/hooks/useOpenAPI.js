import { useState, useEffect } from "react";
import useSettings from './useSettings';

const useOpenAPI = (url) => {
  const settings = useSettings();
  const _url = url || settings.apiURL;
  const [openAPI, setOpenAPI] = useState({});

  useEffect(() => {
    fetch(_url)
      .then((response) => response.json())
      .then((data) => setOpenAPI(data));
  }, [_url]);

  return openAPI;
};

export default useOpenAPI;
