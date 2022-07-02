import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { addBill } from "../../store/bills.js";
import { ValidationError } from "../../utils/validationError";

function AddFriendBill() {
  const dispatch = useDispatch();
  const history = useHistory();

  const [friends, setFriends] = useState([]);
  const [users, setUsers] = useState([]);
  const sessionUser = useSelector((state) => state.session.user);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/users/");
      const responseData = await response.json();
      setUsers(responseData.users);
    }
    fetchData();
  }, []);

  console.log("USERS", users);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`/api/friends/${sessionUser.id}`);
      const responseData = await response.json();
      setFriends(Object.values(responseData));
    }
    fetchData();
  }, []);

  //   console.log(friends)
  const addFriendToBill = (friend) => {
    async function fetchData() {
      const userFriend = users.filter((user) => user.username === friend);
      console.log(userFriend[0].id, "USERFIREND");
      const response = await fetch(
        `/api/bills/add-bill-friends/${userFriend[0].id}`
      );
      history.push("/bills");
      return response;
    }
    fetchData();
  };

  console.log("FRIENDS", friends);

  return (
    <div>
      <h2>Assign friends to bill:</h2>
      {friends[0]?.length > 0 ? (
        friends[0]?.map((friend) => (
          <ul key={friend}>
            <button onClick={() => addFriendToBill(friend)}>{friend}</button>
          </ul>
        ))
      ) : (
        <div>
          <p>You have no friends! Click continue to view your bills.</p>
          <a href="/bills">
            <button>Continue</button>
          </a>
        </div>
      )}
    </div>
  );
}

export default AddFriendBill;
