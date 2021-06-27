import React from 'react';

const Loader = ({loading, children}) => {
    if (loading) {
        return <div>Loading...</div>;
    }

    return <>{children}</>;
}

export default Loader;
