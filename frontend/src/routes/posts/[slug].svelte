<script context="module">
  // @ts-ignore
  export const load = async ({params, fetch}) => {
    const slug = params.slug;
    const url = `http://127.0.0.1:8000/posts/${slug}`;
    const response = await fetch(url);
    const post = await response.json();
    return {props : {post}};
  }
</script>
<script lang="ts">
  import type { Post} from "../../stores/posts"
  export let  post : Post;
</script>

<h2>{post.title}</h2>
{#each post.categories as category}
<span>{category}</span>
{/each}
<p>{post.body}</p>
