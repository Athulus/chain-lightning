import boto3

db = boto3.client('dynamodb')

#print(db.list_tables())

long_entry = '''
<h1>I don't know what you're talking about. I am a member of the Imperial Senate on a diplomatic mission to Alderaan--</h1>
<p>In my experience, there is no such thing as luck. Don't underestimate the Force. Kid, I've flown from one side of this galaxy to the other. I've seen a lot of strange stuff, but I've never seen anything to make me believe there's one all-powerful Force controlling everything. There's no mystical energy field that controls my destiny. It's all a lot of simple tricks and nonsense.</p>
<p>Don't act so surprised, Your Highness. You weren't on any mercy mission this time. Several transmissions were beamed to this ship by Rebel spies. I want to know what happened to the plans they sent you. <strong> What good is a reward if you ain't around to use it?</strong> <em> Besides, attacking that battle station ain't my idea of courage.</em> It's more like…suicide.</p>
<h2>She must have hidden the plans in the escape pod. Send a detachment down to retrieve them, and see to it personally, Commander. There'll be no one to stop us this time!</h2>
<p>Look, I can take you as far as Anchorhead. You can get a transport there to Mos Eisley or wherever you're going. I want to come with you to Alderaan. There's nothing for me here now. I want to learn the ways of the Force and be a Jedi, like my father before me.</p>
<ol>
<li>She must have hidden the plans in the escape pod. Send a detachment down to retrieve them, and see to it personally, Commander. There'll be no one to stop us this time!</li><li>Partially, but it also obeys your commands.</li><li>The plans you refer to will soon be back in our hands.</li>
</ol>

<h3>You're all clear, kid. Let's blow this thing and go home!</h3>
<p>No! Alderaan is peaceful. We have no weapons. You can't possibly… The plans you refer to will soon be back in our hands. I suggest you try it again, Luke. This time, let go your conscious self and act on instinct.</p>
<ul>
<li>I find your lack of faith disturbing.</li><li>Dantooine. They're on Dantooine.</li><li>You are a part of the Rebel Alliance and a traitor! Take her away!</li>
</ul>

<p>I suggest you try it again, Luke. This time, let go your conscious self and act on instinct. Obi-Wan is here. The Force is with him. What good is a reward if you ain't around to use it? Besides, attacking that battle station ain't my idea of courage. It's more like…suicide.</p>
<p>The Force is strong with this one. I have you now. What good is a reward if you ain't around to use it? Besides, attacking that battle station ain't my idea of courage. It's more like…suicide. Dantooine. They're on Dantooine.</p>
<p>In my experience, there is no such thing as luck. You are a part of the Rebel Alliance and a traitor! Take her away! Still, she's got a lot of spirit. I don't know, what do you think? What good is a reward if you ain't around to use it? Besides, attacking that battle station ain't my idea of courage. It's more like…suicide.</p>
<p>But with the blast shield down, I can't even see! How am I supposed to fight? As you wish. I want to come with you to Alderaan. There's nothing for me here now. I want to learn the ways of the Force and be a Jedi, like my father before me.</p>
<p>You mean it controls your actions? The Force is strong with this one. I have you now. I need your help, Luke. She needs your help. I'm getting too old for this sort of thing. The more you tighten your grip, Tarkin, the more star systems will slip through your fingers.</p>
<p>As you wish. What good is a reward if you ain't around to use it? Besides, attacking that battle station ain't my idea of courage. It's more like…suicide. Hokey religions and ancient weapons are no match for a good blaster at your side, kid.</p>
<p>What?! Don't be too proud of this technological terror you've constructed. The ability to destroy a planet is insignificant next to the power of the Force. You mean it controls your actions? You mean it controls your actions?</p>
<p>You are a part of the Rebel Alliance and a traitor! Take her away! I suggest you try it again, Luke. This time, let go your conscious self and act on instinct. The plans you refer to will soon be back in our hands.</p>
<p>Don't be too proud of this technological terror you've constructed. The ability to destroy a planet is insignificant next to the power of the Force. Hokey religions and ancient weapons are no match for a good blaster at your side, kid.</p>
<p>A tremor in the Force. The last time I felt it was in the presence of my old master. Obi-Wan is here. The Force is with him. Ye-ha! Look, I ain't in this for your revolution, and I'm not in it for you, Princess. I expect to be well paid. I'm in it for the money.</p>
<p>All right. Well, take care of yourself, Han. I guess that's what you're best at, ain't it? A tremor in the Force. The last time I felt it was in the presence of my old master. Look, I ain't in this for your revolution, and I'm not in it for you, Princess. I expect to be well paid. I'm in it for the money.</p>
'''

entry = {
    'id': {'N':'2'},
    'crated_date':{'S':'2017-10-01'},
    'tags': {'SS':['useless','filler text']},
    'body':{'S':'long_entry'}
}

db.put_item(TableName='blog-dev-entryTable', Item=entry)

print(db.get_item(TableName='blog-dev-entryTable',Key={'id':{'N':'1'}}))

print(db.scan(TableName='blog-dev-entryTable')['Items'])