<script>
	import { fade, slide, scale } from 'svelte/transition';
	import { flip } from 'svelte/animate';
	export let sunrise;
	export let sunset;
</script>

<div in:slide class="results">
	<div class="one_result">
		<img src="/images/sunrise.svg"  alt="Sunrise icon">
		{sunrise}
	</div>
	<div class="one_result">
		<img src="/images/sunset.svg"  alt="Sunset icon">
		{sunset}
	</div>
</div>

<style>
	.results{
		width: 400px;
		margin: 0 auto;
		text-align: center;
	}
	img{
		width: 100px;
		vertical-align:middle;
		padding-right: 25px;
	}
	.one_result{
		margin: 18px auto;
	}

</style>