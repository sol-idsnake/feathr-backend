class Post:
    def __init__(self,
                 name: str,
                 slug: str,
                 content: str):
        self.name = name
        self.slug = slug
        self.content = content


posts = [
    Post(
        name="Florida summer right around the corner",
        slug="florida-summer-right-around-the-corner",
        id="ea1506ae",
        content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ),
    Post(
        name="Florida man rides Alligator to work",
        slug="florida-man-rides-alligator-to-work",
        id="6fabf381",
        content="Viverra adipiscing at in tellus integer feugiat scelerisque varius morbi. Fames ac turpis egestas sed tempus. Libero enim sed faucibus turpis. Molestie nunc non blandit massa enim nec dui nunc mattis. Sapien et ligula ullamcorper malesuada proin libero nunc consequat. Montes nascetur ridiculus mus mauris vitae. Accumsan tortor posuere ac ut. In nulla posuere sollicitudin aliquam ultrices sagittis. Integer eget aliquet nibh praesent tristique magna sit. Et netus et malesuada fames ac turpis. Cras tincidunt lobortis feugiat vivamus at augue eget arcu."
    ),
    Post(
        name="Lorem Ipsum has reached new heights",
        slug="lorem-ipsum-has-reached-new-heights",
        id="56f9a5cc",
        content="In vitae turpis massa sed elementum. Augue interdum velit euismod in pellentesque. Ornare arcu odio ut sem. Sed felis eget velit aliquet sagittis id consectetur purus ut. Faucibus nisl tincidunt eget nullam non nisi est. Pharetra vel turpis nunc eget lorem dolor sed viverra ipsum. Auctor eu augue ut lectus arcu bibendum at."
    ),
]
