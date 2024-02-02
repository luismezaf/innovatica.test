import React from "react";

type BasePageProps = {
  children: React.ReactNode;
  options?: {
    width?: string;
    height?: string;
  };
};

export default function BasePage({ children, options }: BasePageProps) {
  return (
    <div
      style={{
        width: "100vw",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "white",
        color: "black",
      }}
    >
      <div
        style={{
          width: options?.width || "70vw",
          height: options?.height || "100%",
        }}
      >
        <div
          style={{
            padding: "16px",
          }}
        >
          {children}
        </div>
      </div>
    </div>
  );
}
