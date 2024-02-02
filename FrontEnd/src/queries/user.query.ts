import { AxiosError, AxiosResponse } from "axios";
import { useMutation, useQuery } from "react-query";
import { api } from "../axios";
import { useState } from "react";
import { useGetAllProducts } from "./product.query";

type LoginResponse = {
  access: string;
  refresh: string;
};

type LoginRequest = {
  username: string;
  password: string;
};

type UserProfile = {
  firstName: string;
  lastName: string;
  username: string;
  email: string;
};

export function useLogin() {
  const { refetchUserProfile } = useGetUserProfile();

  const { mutate, isLoading, error } = useMutation<
    AxiosResponse<LoginResponse>,
    AxiosError<LoginRequest & { detail: string }>,
    LoginRequest
  >((requestData) => api.post("auth/login/", requestData), {
    onSuccess: ({ data }) => {
      api.defaults.headers.common.Authorization = `Bearer ${data.access}`;
      refetchUserProfile();
    },
  });

  function logout() {
    api.defaults.headers.common.Authorization = undefined;
    refetchUserProfile();
  }

  return {
    logout,
    login: mutate,
    isLoggingIn: isLoading,
    loginError: error?.response?.data,
  };
}

export function useGetUserProfile() {
  function isLogged() {
    return Boolean(api.defaults.headers.common.Authorization);
  }

  const { data, isLoading, error, refetch } = useQuery<
    AxiosResponse<UserProfile>,
    AxiosError
  >(["user-profile"], () => api.get("profile/"), {
    enabled: isLogged(),
  });

  return {
    isLogged,
    userProfile: data?.data,
    getUserProfileError: error?.response?.data,
    isGettingUserProfile: isLoading,
    refetchUserProfile: refetch,
  };
}
