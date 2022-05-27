<svelte:head>
  <title>{post.title}</title>
</svelte:head>

<h2>{post.title}</h2>
{post.created_at} | Categories :
{#each post.categories as category}
<a href={`/categories/${category}`}><span>{category}</span></a>
{/each}
<p>{post.body}</p>

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