import { useEffect, useState } from "react";
import useSettings from "./useSettings";

const useFetch = (url) => {
  const settings = useSettings();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    (async () => {
      try {
        const response = await fetch(`${settings.apiBaseURL}${url}`);
        const json = await response.json();
        setData(json);
      } catch (err) {
        setError(`${err}`);
      } finally {
        setLoading(false);
      }
    })();
  }, [url]);

  return [data, loading, error];
};

export default useFetch;
