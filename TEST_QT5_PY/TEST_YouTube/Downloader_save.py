# !   p y t h o n 3  
 f r o m   p y t u b e   i m p o r t   Y o u T u b e  
 f r o m   P y Q t 5   i m p o r t   Q t W i d g e t s  
 f r o m   P y Q t 5   i m p o r t   Q t G u i  
 f r o m   P y Q t 5 . Q t C o r e   i m p o r t   *  
 i m p o r t   o s  
 i m p o r t   s y s  
  
  
 c l a s s   M a i n W i n d o w ( Q t W i d g e t s . Q W i d g e t ) :  
         d e f   _ _ i n i t _ _ ( s e l f ) :  
                 s u p e r ( ) . _ _ i n i t _ _ ( )  
  
                 s e l f . i n i t _ u i ( )  
  
         d e f   i n i t _ u i ( s e l f ) :  
                 s e l f . s e t W i n d o w T i t l e ( ' Y o u D o w n l o a d ' )  
                 s e l f . s e t F i x e d S i z e ( 4 7 5 ,   3 2 5 )  
                 #   F o n t s  
                 t i t l e _ f o n t   =   Q t G u i . Q F o n t ( ' T i m e s ' ,   2 4 ,   Q t G u i . Q F o n t . B o l d )  
                 l a b e l _ f o n t   =   Q t G u i . Q F o n t ( ' T i m e s ' ,   8 ,   Q t G u i . Q F o n t . B o l d )  
                 #   M a i n   t i t l e  
                 s e l f . t i t l e   =   Q t W i d g e t s . Q L a b e l ( " Y o u D o w n l o a d " )  
                 s e l f . t i t l e . s e t F o n t ( t i t l e _ f o n t )  
                 s e l f . t i t l e . s e t A l i g n m e n t ( Q t . A l i g n B o t t o m )  
                 #   P l a y   b u t t o n   i m a g e  
                 s e l f . p l a y _ b u t t o n   =   Q t W i d g e t s . Q L a b e l ( )  
                 s e l f . p l a y _ b u t t o n . s e t P i x m a p ( Q t G u i . Q P i x m a p ( ' p l a y b u t t o n . p n g ' ) )  
  
                 t i t l e _ f r a m e   =   Q t W i d g e t s . Q H B o x L a y o u t ( )  
                 t i t l e _ f r a m e . a d d W i d g e t ( s e l f . t i t l e )  
                 t i t l e _ f r a m e . a d d S t r e t c h ( )  
                 t i t l e _ f r a m e . a d d W i d g e t ( s e l f . p l a y _ b u t t o n )  
                 t i t l e _ f r a m e . a d d S t r e t c h ( )  
  
                 # E n t r y   b o x   f o r   y o u t u b e   l i n k  
                 s e l f . v i d e o _ l i n k _ e n t r y   =   Q t W i d g e t s . Q L i n e E d i t ( )  
                 s e l f . v i d e o _ e n t r y _ t e x t   =   Q t W i d g e t s . Q L a b e l ( ' V i d e o   L i n k : ' )  
                 s e l f . v i d e o _ e n t r y _ t e x t . s e t F o n t ( l a b e l _ f o n t )  
  
                 #   F r a m e   f o r   y o u t u b e   l i n k   e n t r y  
                 v i d e o _ l i n k _ f r a m e   =   Q t W i d g e t s . Q H B o x L a y o u t ( )  
                 v i d e o _ l i n k _ f r a m e . a d d W i d g e t ( s e l f . v i d e o _ e n t r y _ t e x t )  
                 v i d e o _ l i n k _ f r a m e . a d d W i d g e t ( s e l f . v i d e o _ l i n k _ e n t r y )  
                 v i d e o _ l i n k _ f r a m e . i n s e r t S p a c i n g ( 2 , 5 0 )  
  
                 #   E d i t   T i t l e  
                 s e l f . t i t l e _ l a b e l   =   Q t W i d g e t s . Q L a b e l ( ' F i l e n a m e : ' )  
                 s e l f . t i t l e _ l a b e l . s e t A l i g n m e n t ( Q t . A l i g n R i g h t )  
                 s e l f . t i t l e _ l a b e l . s e t F o n t ( l a b e l _ f o n t )  
                 s e l f . t i t l e _ e n t r y   =   Q t W i d g e t s . Q L i n e E d i t ( )  
  
                 # v i d e o   t i t l e   f r a m e  
                 v i d _ t i t l e _ f r m   =   Q t W i d g e t s . Q H B o x L a y o u t ( )  
                 v i d _ t i t l e _ f r m . a d d W i d g e t ( s e l f . t i t l e _ l a b e l )  
                 v i d _ t i t l e _ f r m . a d d W i d g e t ( s e l f . t i t l e _ e n t r y )  
                 v i d _ t i t l e _ f r m . i n s e r t S p a c i n g ( 2 , 5 0 )  
  
                 #   C h e c k   b o x e s   f r a m e  
                 s e l f . a u d i o _ o n l y _ c b   =   Q t W i d g e t s . Q C h e c k B o x ( ' A u d i o   O n l y ' )  
                 c h k b o x _ f r m   =   Q t W i d g e t s . Q H B o x L a y o u t ( )  
                 c h k b o x _ f r m . a d d W i d g e t ( s e l f . a u d i o _ o n l y _ c b )  
                 c h k b o x _ f r m . a d d S t r e t c h ( )  
  
                 #   D o w n l o a d   /   C h a n g e   d i r   b u t t o n s  
                 s e l f . c h a n g e d i r _ b u t t o n   =   Q t W i d g e t s . Q P u s h B u t t o n ( " C h a n g e   D i r " )  
                 s e l f . c h a n g e d i r _ b u t t o n . c l i c k e d . c o n n e c t ( s e l f . c h a n g e _ s a v e _ p a t h )  
                 s e l f . d o w n l o a d _ b u t t o n   =   Q t W i d g e t s . Q P u s h B u t t o n ( " D o w n l o a d " )  
                 s e l f . d o w n l o a d _ b u t t o n . c l i c k e d . c o n n e c t ( s e l f . d o w n l o a d )  
                 b u t t o n _ f r m   =   Q t W i d g e t s . Q H B o x L a y o u t ( )  
                 b u t t o n _ f r m . a d d W i d g e t ( s e l f . d o w n l o a d _ b u t t o n )  
                 b u t t o n _ f r m . a d d W i d g e t ( s e l f . c h a n g e d i r _ b u t t o n )  
                 b u t t o n _ f r m . a d d S t r e t c h ( )  
  
                 #   D o w n l o a d   t h r e a d  
                 s e l f . d o w n l o a d e r   =   D o w n l o a d e r ( s e l f )  
                 s e l f . d o w n l o a d e r . p r o c e s s S i g n a l . c o n n e c t ( s e l f . u p d a t e _ p r o g r e s s b a r )  
  
  
                 #   S a v e   d e s t i n a t i o n  
                 s e l f . p a t h _ l a b e l   =   Q t W i d g e t s . Q L a b e l ( " D o w n l o a d   D e s t i n a t i o n : " )  
                 s e l f . p a t h _ l a b e l . s e t F o n t ( l a b e l _ f o n t )  
                 s e l f . p a t h _ v a r   =   o s . p a t h . e x p a n d u s e r ( ' ~ ' )  
                 s e l f . p a t h _ d e s t i n a t i o n   =   Q t W i d g e t s . Q L a b e l ( )  
                 s e l f . p a t h _ d e s t i n a t i o n . s e t T e x t ( s e l f . p a t h _ v a r )  
  
                 #   S a v e   p a t h   f r a m e  
                 s a v e _ p a t h _ f r a m e   =   Q t W i d g e t s . Q H B o x L a y o u t ( )  
                 s a v e _ p a t h _ f r a m e . a d d W i d g e t ( s e l f . p a t h _ l a b e l )  
                 s a v e _ p a t h _ f r a m e . a d d W i d g e t ( s e l f . p a t h _ d e s t i n a t i o n )  
                 s a v e _ p a t h _ f r a m e . a d d S t r e t c h ( )  
  
                 #   p r o g r e s s   b a r  
                 s e l f . p r o g r e s s   =   Q t W i d g e t s . Q P r o g r e s s B a r ( )  
  
                 #   M a i n   l a y o u t   o f   w i n d o w  
                 m a i n _ w i n d o w _ f r a m e   =   Q t W i d g e t s . Q V B o x L a y o u t ( )  
                 m a i n _ w i n d o w _ f r a m e . a d d L a y o u t ( t i t l e _ f r a m e )  
                 m a i n _ w i n d o w _ f r a m e . i n s e r t S p a c i n g ( 1 ,   1 5 )  
                 m a i n _ w i n d o w _ f r a m e . a d d L a y o u t ( v i d e o _ l i n k _ f r a m e )  
                 m a i n _ w i n d o w _ f r a m e . a d d L a y o u t ( v i d _ t i t l e _ f r m )  
                 m a i n _ w i n d o w _ f r a m e . a d d L a y o u t ( c h k b o x _ f r m )  
                 m a i n _ w i n d o w _ f r a m e . a d d L a y o u t ( s a v e _ p a t h _ f r a m e )  
                 m a i n _ w i n d o w _ f r a m e . a d d L a y o u t ( b u t t o n _ f r m )  
                 m a i n _ w i n d o w _ f r a m e . a d d W i d g e t ( s e l f . p r o g r e s s )  
  
                 s e l f . s e t L a y o u t ( m a i n _ w i n d o w _ f r a m e )  
                 s e l f . s h o w ( )  
  
         d e f   c h a n g e _ s a v e _ p a t h ( s e l f ) :  
                 f i l e   =   s t r ( Q t W i d g e t s . Q F i l e D i a l o g . g e t E x i s t i n g D i r e c t o r y ( s e l f ,   " S e l e c t   D i r e c t o r y " ) )  
                 s e l f . p a t h _ d e s t i n a t i o n . s e t T e x t ( f i l e )  
  
         d e f   d o w n l o a d ( s e l f ) :  
                 i f   s e l f . a u d i o _ o n l y _ c b . i s C h e c k e d ( ) :  
                         s e l f . d o w n l o a d e r . d o w n l o a d _ v i d e o ( s e l f . v i d e o _ l i n k _ e n t r y . t e x t ( ) ,   s e l f . p a t h _ d e s t i n a t i o n . t e x t ( ) ,   a u d i o _ o n l y = 1 ,   f i l e _ n a m e = s e l f . t i t l e _ e n t r y . t e x t ( ) )  
                 e l s e :  
                         s e l f . d o w n l o a d e r . d o w n l o a d _ v i d e o ( s e l f . v i d e o _ l i n k _ e n t r y . t e x t ( ) ,   s e l f . p a t h _ d e s t i n a t i o n . t e x t ( ) ,   f i l e _ n a m e = s e l f . t i t l e _ e n t r y . t e x t ( ) )  
  
         d e f   u p d a t e _ p r o g r e s s b a r ( s e l f ,   p e r c e n t a g e ) :  
                 s e l f . p r o g r e s s . s e t V a l u e ( p e r c e n t a g e )  
                 i f   i n t ( p e r c e n t a g e )   = =   1 0 0 :  
                         s e l f . c o m p l e t e d ( )  
  
         d e f   c o m p l e t e d ( s e l f ) :  
                 m s g   =   Q t W i d g e t s . Q M e s s a g e B o x ( )  
                 m s g . s e t I c o n ( Q t W i d g e t s . Q M e s s a g e B o x . I n f o r m a t i o n )  
                 m s g . s e t W i n d o w T i t l e ( " C o m p l e t e d " )  
                 m s g . s e t T e x t ( ' V i d e o   D o w n l o a d e d   s u c c e s s f u l l y ' )  
                 m s g . e x e c _ ( )  
  
  
  
  
 c l a s s   D o w n l o a d e r ( Q T h r e a d ) :  
  
         p r o c e s s S i g n a l   =   p y q t S i g n a l ( f l o a t )  
  
         d e f   _ _ i n i t _ _ ( s e l f ,   p a r e n t = N o n e ) :  
                 s u p e r ( D o w n l o a d e r ,   s e l f ) . _ _ i n i t _ _ ( p a r e n t = p a r e n t )  
                 s e l f . p a t h   =   N o n e  
                 s e l f . u r l   =   N o n e  
                 s e l f . v i d e o   =   N o n e  
                 s e l f . s t r e a m   =   N o n e  
                 s e l f . a u d i o _ o n l y   =   N o n e  
  
         d e f   d o w n l o a d _ v i d e o ( s e l f ,   u r l ,   p a t h ,   a u d i o _ o n l y = 0 ,   f i l e _ n a m e = N o n e ) :  
                 s e l f . p a t h   =   p a t h  
                 s e l f . u r l   =   u r l  
                 s e l f . a u d i o _ o n l y   =   a u d i o _ o n l y  
                 s e l f . f i l e _ n a m e   =   f i l e _ n a m e  
  
                 s e l f . s t a r t ( )  
  
         d e f   r u n ( s e l f ) :  
                 s e l f . v i d e o   =   Y o u T u b e ( s e l f . u r l )  
                 s e l f . v i d e o . r e g i s t e r _ o n _ p r o g r e s s _ c a l l b a c k ( s e l f . r e t u r n _ p r o g r e s s )  
                 i f   s e l f . a u d i o _ o n l y   = =   1 :  
                         s e l f . s t r e a m   =   s e l f . v i d e o . s t r e a m s . f i l t e r ( o n l y _ a u d i o = T r u e ) . f i r s t ( )  
                 e l s e :  
                         s e l f . s t r e a m   =   s e l f . v i d e o . s t r e a m s . f i r s t ( )  
                 s e l f . s t r e a m . d o w n l o a d ( s e l f . p a t h ,   s e l f . f i l e _ n a m e )  
  
         d e f   r e t u r n _ p r o g r e s s ( s e l f ,   s t r e a m ,   c h u n k ,   f i l e _ h a n d l e ,   b y t e s _ r e m a i n i n g ) :  
                 p e r c e n t a g e   =   ( 1   -   b y t e s _ r e m a i n i n g   /   s e l f . s t r e a m . f i l e s i z e )   *   1 0 0  
                 s e l f . p r o c e s s S i g n a l . e m i t ( p e r c e n t a g e )  
  
  
 a p p   =   Q t W i d g e t s . Q A p p l i c a t i o n ( s y s . a r g v )  
 w i n d o w   =   M a i n W i n d o w ( )  
 a p p . e x i t ( a p p . e x e c _ ( ) )  
 